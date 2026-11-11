const {chromium}=require('playwright'); const fs=require('fs');
(async()=>{
 const names=process.argv.slice(2);
 const b=await chromium.launch();
 for(const n of names){
  const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+process.cwd()+'/'+n+'.html'); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({path:n+'.png'});
  await p.pdf({path:n+'.pdf',width:'1920px',height:'1080px',printBackground:true,pageRanges:'1'});
  await p.close();
 }
 await b.close();
})();
