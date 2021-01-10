import * as React from 'react'
import { Catalog } from '../../interfaces/models';
import ListItem from './ListItem';

type Props = {
  items: Catalog[]
}

const List = ({ items }: Props) => (
  <ul>
    {items.map((item) => (
      <li key={item.id}>
        <ListItem data={item} />
      </li>
    ))}
  </ul>
)

export default List
