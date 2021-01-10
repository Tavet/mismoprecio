import { NextApiRequest, NextApiResponse } from 'next'
import { sampleCatalogData } from '../../../utils/sample-data'

const handler = (_req: NextApiRequest, res: NextApiResponse) => {
  try {
    if (!Array.isArray(sampleCatalogData)) {
      throw new Error('Cannot find catalog data')
    }

    res.status(200).json(sampleCatalogData)
  } catch (err) {
    res.status(500).json({ statusCode: 500, message: err.message })
  }
}

export default handler
