const { nodeFileTrace } = require("@vercel/nft");
const files = ["./src/main.js"];
nodeFileTrace(files).then(({ fileList }) => {
  console.log(fileList);
});
