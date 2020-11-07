import { css } from "linaria";

const wrapper = css`
  display: block;
  width: 300px;
  height: 300px;
  margin: 12px auto;
`;

export const Icon = () => {
  return (
    <img
      className={wrapper}
      src="https://shinyaigeek.dev/icon_transparent.png"
    />
  );
};
