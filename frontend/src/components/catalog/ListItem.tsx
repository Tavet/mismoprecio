import React from 'react'
import Link from 'next/link'
import { Catalog } from '../../interfaces/models';

type Props = {
  data: Catalog
}

const ListItem = ({ data }: Props) => (
  <Link href="/clothes/[id]" as={`/clothes/${data.id}`}>
    <a>
      {data.id}: {data.name}
    </a>
  </Link>
)

export default ListItem
