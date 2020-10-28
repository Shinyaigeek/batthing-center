import { Trans } from "@lingui/macro";

export const Hello = () => {
  return (
    <>
      <div>
        <Trans>Hello</Trans>
      </div>
      <style jsx>{`
        div {
            font-weight: bold;
            font-size: 48px;
            animation: 1s linear 1s infinite running animation;
            width: 100vw;
            text-align: center;
        }
        @keyframes animation {
            from {
                transform: scaleX(0);
            }
            to {
                transform: scaleX(1);
            }
        }
      `}</style>
    </>
  );
};
