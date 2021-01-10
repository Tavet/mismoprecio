import { Catalog } from '../../interfaces/models'
import { GetStaticProps } from 'next'
import { sampleCatalogData } from './../../utils/sample-data';

type Props = {
    items: Catalog[]
}


export const getStaticProps: GetStaticProps = async () => {
    const items: Catalog[] = sampleCatalogData
    return { props: { items } }
  }