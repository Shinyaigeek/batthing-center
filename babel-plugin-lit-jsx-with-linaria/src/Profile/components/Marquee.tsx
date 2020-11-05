import { styled } from "linaria/react";

interface Props {
  content: string;
}

export const Marquee = ({ content }: Props) => {
  return <Container>{content}</Container>;
};

const Container = styled.div`
  color: blue;
`;
