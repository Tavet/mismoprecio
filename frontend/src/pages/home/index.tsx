import Link from 'next/link'
import Layout from '../../components/general/Layout'
import { Button } from 'reactstrap';


const WithStaticProps = () => (
    <Layout title="Users List | Next.js + TypeScript Example">
        <h1>HOMEEEEEEEEEEEEEEE List</h1>
        <Button color="danger">Danger!</Button>
        <p>
            <Link href="/">
                <a>Go home</a>
            </Link>
        </p>
    </Layout>
)



export default WithStaticProps
