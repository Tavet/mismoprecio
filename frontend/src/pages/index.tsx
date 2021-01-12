// import Home from './home'
import 'bootstrap/dist/css/bootstrap.min.css';
import './../styles/general.global.scss'
import './style.scss'

const IndexPage = () => (
  <div className="muy-pronto">
    <div className="box">
      <img className="logo" src={require('./../static/images/mismoprecio.svg')} width="46" height="46" />
      <h1>
        Espéranos. ¡Muy pronto!
    </h1>
      <h3>Llegaremos con muchas novedades para que puedas buscar tu prenda ó outfit ideal al <strong>mismo precio</strong>.</h3>
    </div>
  </div>
)

export default IndexPage
