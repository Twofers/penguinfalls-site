$ErrorActionPreference = 'Stop'
$pfRoot = Split-Path $PSScriptRoot
$pfCatalog = (Get-Content -LiteralPath (Join-Path $pfRoot 'data/app-store-snapshot.json') -Raw | ConvertFrom-Json).results
$pfSlugs = @('twofer','sightlines','penguin-bounce','penguin-slide','penguin-express','penguin-crash')
$pfIndexes = @(@(0,1,2),@(0,2,3),@(1,2,3),@(1,2,3),@(1,0,3),@(2,0,1))
$pfCache = Join-Path $pfRoot '.asset-cache'
New-Item -ItemType Directory -Force -Path $pfCache | Out-Null
for ($pfI=0; $pfI -lt 6; $pfI++) {
    $pfApp = $pfCatalog[$pfI]
    if ($pfApp.sellerName -ne 'Penguin Falls LLC') { throw 'Unexpected app owner' }
    $pfIcon = Join-Path $pfCache ($pfSlugs[$pfI] + '-icon-20260926.webp.jpg')
    if (!(Test-Path -LiteralPath $pfIcon)) { Invoke-WebRequest -Uri $pfApp.artworkUrl512 -OutFile $pfIcon -TimeoutSec 30 }
    for ($pfJ=0; $pfJ -lt 3; $pfJ++) {
        $pfUrl = $pfApp.screenshotUrls[$pfIndexes[$pfI][$pfJ]].Replace('/320x480bb.jpg','/640x1388bb.jpg')
        $pfFile = Join-Path $pfCache ($pfSlugs[$pfI] + '-screen-' + ($pfJ+1) + '-20260926.webp.jpg')
        if (!(Test-Path -LiteralPath $pfFile)) { Invoke-WebRequest -Uri $pfUrl -OutFile $pfFile -TimeoutSec 30 }
    }
    Write-Output ('Downloaded assets: ' + $pfSlugs[$pfI])
}
