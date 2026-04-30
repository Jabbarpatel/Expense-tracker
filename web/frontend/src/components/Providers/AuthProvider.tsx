import React from "react";

type Props = {
  children: React.ReactNode;
};

const AuthProvider = ({ children }: Props) => {
  const token = localStorage.getItem("token");
  if (!token) {
    return;
  }
  return children;
};
export default AuthProvider;
