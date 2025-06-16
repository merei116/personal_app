import type { AppProps } from 'next/app';
import '../app/globals.css';
import Layout from '../components/Layout';
import 'next-pwa/register';
import { useEffect } from 'react';
import { init, getThemeParams } from '../lib/telegram';

function MyApp({ Component, pageProps }: AppProps) {
  useEffect(() => {
    init();
    const theme = getThemeParams();
    if (theme.bg_color) {
      document.body.style.backgroundColor = theme.bg_color;
    }
    if (theme.text_color) {
      document.body.style.color = theme.text_color;
    }
  }, []);

  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  );
}

export default MyApp;
