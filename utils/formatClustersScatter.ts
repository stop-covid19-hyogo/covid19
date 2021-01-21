import { convertDateToISO8601Format } from '@/utils/formatDate'

interface DataObject {
  日付: string
  [key: string]: number | string
}

export type ChildGraphDataType = {
  x: string
  y: number
  label: number
}

export type GraphDataType = {
  datasets: ChildGraphDataType[]
  clusters: string[]
  labels: string[]
}

export default (data: DataObject[]) => {
  const clusters = Object.keys(data[0]).filter((s) => s !== '日付')
  clusters.push('')
  clusters.reverse()
  const graphData: GraphDataType = {
    datasets: [],
    clusters,
    labels: [],
  }

  data.forEach((d, i) => {
    if (i === 0) {
      const prevDate = new Date(d['日付'])
      prevDate.setDate(prevDate.getDate() - 1)
      const prevDateLabel = convertDateToISO8601Format(prevDate.toISOString())
      graphData.labels.push(prevDateLabel)
    }
    const dateLabel = convertDateToISO8601Format(d['日付'])
    graphData.labels.push(dateLabel)
    clusters.forEach((dl, j) => {
      if (dl !== '') {
        const patients = d[dl]
        if (patients !== 0) {
          graphData.datasets.push(<ChildGraphDataType>{
            x: dateLabel,
            y: j,
            label: patients,
          })
        }
      }
    })
  })
  return graphData
}
