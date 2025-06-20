import type { AppProps } from 'next/app';
import '../app/globals.css';
import Layout from '../components/Layout';
import 'next-pwa/register';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  );
}

export default MyApp;
