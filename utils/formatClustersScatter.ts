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
  const clusters = Object.keys(data[0])
    .reverse()
    .filter(s => s !== '日付')
  const graphData: GraphDataType = {
    datasets: [],
    clusters,
    labels: []
  }

  data.forEach(d => {
    const date = new Date(d['日付'])
    const dateLable = `${date.getMonth() + 1}/${date.getDate()}`
    graphData.labels.push(dateLable)
    clusters.forEach((dl, j) => {
      const patients = d[dl]
      if (patients !== 0) {
        graphData.datasets.push(<ChildGraphDataType>{
          x: dateLable,
          y: j,
          label: patients
        })
      }
    })
  })
  return graphData
}
