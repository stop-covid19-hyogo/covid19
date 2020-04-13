export type SurfaceStyle = {
  strokeColor: string
  fillColor: string
}

const surfaceStyleA: SurfaceStyle = {
  strokeColor: '#016984',
  fillColor: '#006687'
}

const surfaceStyleB: SurfaceStyle = {
  strokeColor: '#016984',
  fillColor: '#01a0c7'
}

const surfaceStyleC: SurfaceStyle = {
  strokeColor: '#016984',
  fillColor: '#4bcaec'
}

export function getGraphSeriesStyle(seriesLength: number) {
  switch (seriesLength) {
    case 1:
      return [surfaceStyleB]
    case 2:
      return [surfaceStyleA, surfaceStyleC]
    default:
      return [surfaceStyleA, surfaceStyleB, surfaceStyleC]
  }
}
