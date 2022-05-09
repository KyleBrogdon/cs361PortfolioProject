const fs = require("fs");
const puppeteer = require("puppeteer");

const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function scrapeImages(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  const imgs = await page.$$eval("img", (wallpapers) => {
    return wallpapers.map((x) => x.src);
  });
  return imgs;
  await browser.close();
}

async function getImages() {
  let watchRequest = true;
  // while (watchRequest) {
  await delay(1000); // pause one second
  fs.readFile("image_request.txt", async function (err, line) {
    while (watchRequest) {
      if (err) console.log(err);
      const data = line.toString();
      if (data === "fetch_images") {
        const imageurlArray = await scrapeImages(
          "https://www.freeimages.com/premium/animals-wildlife"
        );
        // console.log(imageurlArray.slice(10, 40));
        fs.truncate("bg_image_urls.txt", 0, function () {
        //   console.log("bg_image_urls.txt cleared");
        });
        fs.writeFile(
          "bg_image_urls.txt",
          imageurlArray.slice(10, 40).join("\n"),
          function () {
            // console.log("added bg image urls to bg_image_urls");
          }
        );
        break;
      } else {
        continue;
      }
    }
  });
  //   break;
  // }
}
getImages();
