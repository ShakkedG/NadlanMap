const GOVMAP_SCRIPT_ID = 'govmap-api-script'
const GOVMAP_SCRIPT_URL = 'https://www.govmap.gov.il/govmap/api/govmap.api.js'

export function loadGovMapApi() {
  return new Promise((resolve, reject) => {
    if (window.govmap) {
      resolve(window.govmap)
      return
    }

    const existingScript = document.getElementById(GOVMAP_SCRIPT_ID)
    if (existingScript) {
      existingScript.addEventListener('load', () => resolve(window.govmap), { once: true })
      existingScript.addEventListener('error', reject, { once: true })
      return
    }

    const script = document.createElement('script')
    script.id = GOVMAP_SCRIPT_ID
    script.src = GOVMAP_SCRIPT_URL
    script.defer = true
    script.onload = () => {
      if (window.govmap) resolve(window.govmap)
      else reject(new Error('GovMap API loaded, but window.govmap was not found.'))
    }
    script.onerror = () => reject(new Error('Failed to load GovMap API script.'))
    document.head.appendChild(script)
  })
}
