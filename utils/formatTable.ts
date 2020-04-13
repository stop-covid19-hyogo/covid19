import dayjs from 'dayjs'

const headers = [
  { text: 'No', value: 'No' },
  { text: '公表日', value: '公表日' },
  { text: '居住地', value: '居住地' },
  { text: '年代', value: '年代' },
  { text: '性別', value: '性別' } //,
  // { text: '備考', value: '備考' } //,
  // { text: '退院※', value: '退院', align: 'center' }
]

type DataType = {
  No: number
  リリース日: string
  居住地: string | null
  年代: string | null
  性別: '男性' | '女性' | string
  // 備考: string | null
  // 退院: '◯' | null
  [key: string]: any
}

type TableDataType = {
  No: DataType['No']
  公表日: string
  居住地: DataType['居住地']
  年代: DataType['年代']
  性別: DataType['性別'] | '不明'
  // 備考: DataType['備考']
  // 退院: DataType['退院']
}

type TableDateType = {
  headers: typeof headers
  datasets: TableDataType[]
}

/**
 * Format for DataTable component
 *
 * @param data - Raw data
 */
export default (data: DataType[]) => {
  const tableDate: TableDateType = {
    headers,
    datasets: []
  }
  data.forEach(d => {
    const TableRow: TableDataType = {
      No: d.No ?? '不明',
      公表日: dayjs(d['リリース日']).format('MM/DD') ?? '不明',
      居住地: d['居住地'] ?? '調査中',
      年代: d['年代'] ?? '不明',
      性別: d['性別'] ?? '不明',
      // 備考: d['備考'] ?? 'なし' //,
      // 退院: d['退院']
    }
    tableDate.datasets.push(TableRow)
  })
  tableDate.datasets.sort((a, b) =>
    a.公表日 === b.公表日 ? 0 : a.公表日 < b.公表日 ? 1 : -1
  )
  return tableDate
}
