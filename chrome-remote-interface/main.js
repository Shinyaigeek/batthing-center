import CDP from "chrome-remote-interface";

const main = async () => {
  let client;
  try {
    client = await CDP({
      port: 1234,
      host: "localhost"
    });
    const { Page, Audits } = client;
    Audits.enable();
    Audits.issueAdded(params => {
      console.log("Audits🌟 :" + params.issue.code)
    })
    await Page.enable();
    await Page.navigate({ url: "https://www.888.co.jp/" });
    await Page.loadEventFired();
  } catch (err) {
    console.error(err);
  } finally {
    if (client) {
      await client.close();
    }
  }
};

main();
