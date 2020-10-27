import CDP from "chrome-remote-interface";

const main = async () => {
  const client = await (async () => {
    return CDP({
      port: 1234,
      host: "localhost",
    }).catch((err) => {
      console.error(err);
    });
  })();
  const { Page, Audits } = client;
  Audits.enable();
  Audits.issueAdded((params) => {
    console.log("Audits🌟 :" + params.issue.code);
  });
  await Page.enable();
  await Page.navigate({ url: "some url" });
  await Page.loadEventFired();

  if (client) {
    await client.close();
  }
};

main();
