import { Genre } from '../interfaces/enum';
import { Catalog } from '../interfaces/models';

/* Dummy Catalog Data */
export const sampleCatalogData: Catalog[] = [
  {    
    id: 1,
    name: "BOLSO PARA HOMBRE GRANYTO BACK - VERDE OSCURO U",
    description: "Bolso Para Hombre Granyto Back. Importado por Estudio de Moda SAS. NIT: 890926803.",
    reference: "X07424PR163",
    price: 674925,
    oldPrice: 899900,
    discount: 25,
    url: "https://co.diesel.com/bolso-para-hombre-granyto-back--/p",
    image: "https://dieselcolombia.vteximg.com.br/arquivos/ids/302089-498-664/Bolso-Para-Hombre-Granyto-Back--1911.jpg?v=637450380239470000",
    genre: Genre.Male
  }
]
 
 