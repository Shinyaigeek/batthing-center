export interface UserType {
  login: string;
  id: number;
  node_id: string;
  html_url: string;
}

export const User = (props: UserType) => {
  return (
    <>
      <div className="container">
        <div className="name">{props.login}</div>
      </div>
      <style jsx>{`
        .name {
          font-size: 24px;
          font-weight: bold;
        }
        .container {
            border-bottom: 1px solid black;
            width: 80%;
            margin: 12px auto;
        }
      `}</style>
    </>
  );
};
