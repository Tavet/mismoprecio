import React, { ReactNode } from 'react'
import Head from 'next/head'
import Footer from '../Footer';
import Nav from '../navigation';
import './style.scss';

type Props = {
  children?: ReactNode
  title?: string
}

const Layout = ({ children, title = 'This is the default title' }: Props) => (
  <div className="layout">
    <Head>
      <title>{title}</title>
      <meta charSet="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </Head>
    <header>
      <Nav />
    </header>
    {children}
    <Footer />
  </div>
)

export default Layout
