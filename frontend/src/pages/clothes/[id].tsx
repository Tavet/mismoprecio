import { GetStaticProps, GetStaticPaths } from 'next'

import Layout from '../../components/general/layout'
import ListDetail from '../../components/catalog/ListDetail'
import { Catalog } from '../../interfaces/models'
import { sampleCatalogData } from '../../utils/sample-data';

type Props = {
    item?: Catalog
    errors?: string
}

const StaticPropsDetail = ({ item, errors }: Props) => {
    if (errors) {
        return (
            <Layout title="Error | Next.js + TypeScript Example">
                <p>
                    <span style={{ color: 'red' }}>Error:</span> {errors}
                </p>
            </Layout>
        )
    }

    return (
        <Layout
            title={`${item ? item.name : 'User Detail'
                } | Next.js + TypeScript Example`}
        >
            {item && <ListDetail item={item} />}
        </Layout>
    )
}

export default StaticPropsDetail

export const getStaticPaths: GetStaticPaths = async () => {
    const paths = sampleCatalogData.map((user) => ({
        params: { id: user.id.toString() },
    }))

    return { paths, fallback: false }
}

export const getStaticProps: GetStaticProps = async ({ params }) => {
    try {
        const id = params?.id
        const item = sampleCatalogData.find((data) => data.id === Number(id))
        return { props: { item } }
    } catch (err) {
        return { props: { errors: err.message } }
    }
}
