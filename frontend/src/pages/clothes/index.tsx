import { GetStaticProps } from 'next'
import Link from 'next/link'

import Layout from '../../components/general/layout'
import List from '../../components/catalog/List'

import { Catalog } from '../../interfaces/models'
import { sampleCatalogData } from '../../utils/sample-data';

type Props = {
    items: Catalog[]
}

const WithStaticProps = ({ items }: Props) => (
    <Layout title="Users List | Next.js + TypeScript Example">
        <h1>Users List</h1>
        <p>
            Example fetching data from inside <code>getStaticProps()</code>.
    </p>
        <p>You are currently on: /users</p>
        <List items={items} />
        <p>
            <Link href="/">
                <a>Go home</a>
            </Link>
        </p>
    </Layout>
)

export const getStaticProps: GetStaticProps = async () => {
    const items: Catalog[] = sampleCatalogData
    return { props: { items } }
}

export default WithStaticProps
