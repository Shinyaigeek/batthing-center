import { Trans } from "@lingui/macro";

export const Footer = () => {
  return (
    <>
      <footer>
        <Trans>This is Footer</Trans>
      </footer>
      <style jsx>
        {`
          footer {
            color: white;
            background: black;
            width: 100vw;
          }
        `}
      </style>
    </>
  );
};
