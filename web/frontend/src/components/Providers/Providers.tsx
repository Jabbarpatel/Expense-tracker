import React from "react";
import { QueryClient, QueryClientProvider } from "react-query";
import AuthProvider from "./AuthProvider";

type Props = {
  children: React.ReactNode;
};

const queryClient = new QueryClient();

const Providers = ({ children }: Props) => {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>{children}</AuthProvider>
    </QueryClientProvider>
  );
};
export default Providers;
