import * as React from 'react'

import { Catalog } from '../../interfaces/models'

type ListDetailProps = {
  item: Catalog
}

const ListDetail = ({ item: catalog }: ListDetailProps) => (
  <div>
    <h1>Detail for {catalog.name}</h1>
    <p>ID: {catalog.id}</p>
  </div>
)

export default ListDetail
