
const {readFileSync}=require('node:fs');
const {runInNewContext}=require('node:vm');
const assert=require('node:assert/strict');
const code=readFileSync(require('node:path').join(__dirname, '..', 'analytics.js'),'utf8');
function run(host,nav={},path='/') {
 const scripts=[];const win={location:{hostname:host,pathname:path},dispatchEvent(){}};
 runInNewContext(code,{window:win,navigator:nav,document:{addEventListener(){},createElement(){return{};},head:{appendChild(s){scripts.push(s);}}},URL,Set,Element:class{},CustomEvent:class{}});
 return {win,scripts};
}
for(const host of ['127.0.0.1','localhost','candidate.vercel.app'])assert.equal(run(host).scripts.length,0);
assert.equal(run('www.penguinfalls.com',{doNotTrack:'1'}).scripts.length,0);
assert.equal(run('www.penguinfalls.com',{globalPrivacyControl:true}).scripts.length,0);
assert.equal(run('www.penguinfalls.com',{},'/private').scripts.length,0);
const prod=run('www.penguinfalls.com');
assert.equal(prod.scripts.length,1);
const filter=prod.win.vaq[0][1];
assert.equal(filter({url:'https://www.penguinfalls.com/sightlines?email=private#secret'}).url,'https://www.penguinfalls.com/sightlines');
assert.equal(filter({url:'https://www.penguinfalls.com/private?token=private'}),null);
assert.equal(filter({url:'https://foreign.example/sightlines'}),null);
assert.equal(prod.win.vaq.filter(x=>x[0]==='event').length,0);
console.log('Analytics privacy checks passed: preview exclusion, DNT/GPC, path allowlist, query/hash redaction, no custom event submission.');
