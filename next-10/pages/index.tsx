import Image from "next/image";
import { User, UserType } from "../components/User";
import { I18nProvider } from "@lingui/react";
import { Trans } from "@lingui/macro";
import catalogJa from "../locale/ja/messages";
import catalogEn from "../locale/en/messages";
import { Footer } from "../components/Footer";
import { Hey } from "../components/Hey";
import { Switch } from "../components/Switch";

const target = "https://api.github.com/users/Shinyaigeek/following";

interface Props {
  users: UserType[];
  locale: "ja" | "en";
}

const catalogs = {
  en: catalogEn,
  ja: catalogJa,
};

const Home = (props: Props) => {
  return (
    <I18nProvider language={props.locale} catalogs={catalogs}>
      <div>
        <Switch locale={props.locale} />
        <Hey />
        {props.users.map((user) => (
          <User {...user} />
        ))}
        <Footer />
      </div>
    </I18nProvider>
  );
};

export const getServerSideProps = async (context) => {
  const users = await (await fetch(target)).json();
  return {
    props: {
      users,
      locale: context.locale,
    },
  };
};

export default Home;
