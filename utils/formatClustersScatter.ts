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
      const prevDateLable = `${prevDate.getMonth() + 1}/${prevDate.getDate()}`
      graphData.labels.push(prevDateLable)
    }
    const date = new Date(d['日付'])
    const dateLable = `${date.getMonth() + 1}/${date.getDate()}`
    graphData.labels.push(dateLable)
    clusters.forEach((dl, j) => {
      if (dl !== '') {
        const patients = d[dl]
        if (patients !== 0) {
          graphData.datasets.push(<ChildGraphDataType>{
            x: dateLable,
            y: j,
            label: patients,
          })
        }
      }
    })
  })
  return graphData
}
