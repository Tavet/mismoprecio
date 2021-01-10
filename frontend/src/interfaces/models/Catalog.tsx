import { Genre } from "../enum";
import { Store } from "./Store";
import { Subcategory } from "./Subcategory";

export type Catalog = {
    id: number
    name: string
    description: string
    reference: string
    price: number
    oldPrice: number
    discount: number
    url: string
    image: string
    genre: Genre
    store?: Store
    subcategory?: Subcategory
  }