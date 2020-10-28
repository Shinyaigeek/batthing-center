import Link from "next/link";

interface Props {
  locale: "en" | "ja";
}

export const Switch = (props: Props) => {
  return (
    <>
      <button>
        <Link href="/" locale={props.locale === "ja" ? "en" : "ja"}>
          <a>to {props.locale === "ja" ? "en" : "ja"}</a>
        </Link>
      </button>
      <style jsx>{`
        button {
          position: fixed;
          top: 12px;
          right: 36px;
        }
      `}</style>
    </>
  );
};
