export const headers = [
  { text: 'クラスター/感染源', value: 'クラスター' },
  { text: '人数', value: '人数' }
]

interface DataObject {
  [key: string]: number
}

export type TableDataType = {
  クラスター: string
  人数: number
}

type TableClustersType = {
  headers: typeof headers
  datasets: TableDataType[]
}

export default (data: DataObject) => {
  const headerData = Object.keys(data)
  const tableDate: TableClustersType = {
    headers,
    datasets: []
  }
  headerData.forEach(d => {
    const TableRow: TableDataType = {
      クラスター: d,
      人数: data[d]
    }
    tableDate.datasets.push(TableRow)
  })
  // tableDate.datasets.sort((a, b) => (a === b ? 0 : a < b ? 1 : -1))
  return tableDate
}
