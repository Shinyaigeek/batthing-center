import puppeteer from "puppeteer";
import looksSame from "looks-same";

// const URL_A = "http://localhost:5500/";
const URL_A = "https://shinyaigeek.dev/";
const URL_B = "https://hack.nikkei.com/";

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
    await page.setViewport({
      width: 712,
      height: 412,
    });

  const pathA = "dist/a.png";
  const pathB = "dist/b.png";
  const pathDiff = "dist/diff.png";
  page.setDefaultTimeout(999999999);
  await page.goto(URL_A, {
    waitUntil: "networkidle2",
  });
  const bodyHandle = await page.$("body");
  if(!bodyHandle) {
      throw new Error
  }
  const aaa = await bodyHandle.boundingBox();
  if(!aaa) {
      throw new Error
  }
  const { width, height } = aaa;

  
  console.log(width, height)
  await page.screenshot({
    path: pathA,
    // clip: {
    //   x: 0,
    //   y: 0,
    // //   width,
    // //   height,
    // },
    fullPage: true
  });
  await page.goto(URL_B, {
    waitUntil: "load",
  });
  await page.screenshot({
    path: pathB,
    // clip: {
    //   x: 0,
    //   y: 0,
    //   width,
    //   height,
    // },
    fullPage: true
  });

  await new Promise((resolve, reject) =>
    looksSame.createDiff(
      {
        reference: pathA,
        current: pathB,
        diff: pathDiff,
        highlightColor: "#ff00ff",
      },
      (error) => (error ? reject(error) : resolve("ok"))
    )
  );

  await browser.close();
})();
