import { css } from "linaria";

interface Props {
  content: string;
}



const marquee = css`

animation: marquee 4s linear infinite;
text-align: center;

  @keyframes marquee {
    from {
      font-size: 16px;
    }

    to {
      font-size: 48px;
    }
  }
`;

export const Marquee = ({ content }: Props) => {
  return (
      <div className={marquee}>{content}</div>
  );
};
