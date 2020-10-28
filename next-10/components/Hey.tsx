import { Trans } from "@lingui/macro";
import Image from "next/image";
import { Hello } from "./Hello";

export const Hey = () => {
  return (
    <div>
      <Hello />
      <div className="icon">
        <Image
          src="/icon.png"
          alt="monkey"
          width={100}
          height={100}
          className="icon"
        />
      </div>
      <div className="name">
        <Trans>ImShinyai</Trans>
      </div>
      <div className="list">
        <Trans>WhoIFollowing</Trans>
      </div>
      <style jsx>{`
        .icon {
          display: block;
          margin: 4px auto;
          width: 100px;
        }

        .name {
          font-size: 34px;
          text-align: center;
        }

        .list {
          font-size: 24px;
          text-align: center;
        }
      `}</style>
    </div>
  );
};
