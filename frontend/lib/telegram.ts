import '@twa-dev/sdk';

declare global {
  interface Window {
    Telegram?: { WebApp?: any };
  }
}

export const WebApp = typeof window === 'undefined' ? undefined : window.Telegram?.WebApp;

export function init() {
  if (WebApp && typeof WebApp.ready === 'function') {
    WebApp.ready();
  }
}

export function getThemeParams() {
  return WebApp?.themeParams ?? {};
}
