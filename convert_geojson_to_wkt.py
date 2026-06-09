* {
  box-sizing: border-box;
}

html,
body,
#app {
  width: 100%;
  min-height: 100%;
  margin: 0;
}

body {
  font-family: Arial, "Noto Sans Hebrew", sans-serif;
  background: #eef2f7;
  color: #142033;
}

button,
select,
input,
a {
  font: inherit;
}

button {
  cursor: pointer;
}

button:disabled,
select:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.page-shell {
  min-height: 100vh;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.panel {
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.96);
  box-shadow: 0 12px 34px rgba(15, 23, 42, 0.08);
  border: 1px solid rgba(148, 163, 184, 0.25);
}

.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 22px;
  padding: 20px;
}

.eyebrow {
  margin: 0 0 6px;
  color: #2563eb;
  font-weight: 800;
  font-size: 14px;
}

h1,
h2,
p {
  margin-top: 0;
}

h1 {
  margin-bottom: 8px;
  font-size: clamp(26px, 4vw, 42px);
  letter-spacing: -0.03em;
}

h2 {
  margin-bottom: 12px;
  font-size: 18px;
}

.subtitle {
  max-width: 860px;
  margin-bottom: 0;
  color: #64748b;
  line-height: 1.65;
}

.hero-actions,
.controls {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.hero-actions button,
.controls select,
.controls input {
  border: 1px solid #dbe3ef;
  border-radius: 14px;
  padding: 11px 14px;
  background: #f8fafc;
  color: #142033;
}

.hero-actions button {
  border: 0;
  background: #e2e8f0;
  transition: transform 0.15s ease, opacity 0.15s ease;
}

.hero-actions button:hover:not(:disabled) {
  transform: translateY(-1px);
}

.hero-actions .primary {
  background: #2563eb;
  color: white;
}

.controls {
  align-items: end;
  padding: 14px;
}

.controls label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 190px;
  font-weight: 700;
  color: #475569;
}

.controls .search-box {
  flex: 1;
  min-width: 260px;
}

.status-card {
  display: flex;
  align-items: center;
  gap: 10px;
  border-radius: 16px;
  padding: 12px 16px;
  background: #ecfdf5;
  border: 1px solid #bbf7d0;
}

.status-card.error {
  background: #fef2f2;
  border-color: #fecaca;
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  gap: 14px;
  align-items: stretch;
}

.map-card {
  position: relative;
  overflow: hidden;
  min-height: 650px;
  border-radius: 22px;
  background: white;
  box-shadow: 0 12px 34px rgba(15, 23, 42, 0.08);
}

.map {
  width: 100%;
  height: 650px;
}

.loader {
  position: absolute;
  z-index: 10;
  inset: 18px 18px auto auto;
  padding: 10px 14px;
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.94);
  box-shadow: 0 10px 26px rgba(15, 23, 42, 0.16);
  font-weight: 800;
}

.side-panel {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.stats-panel,
.legend-panel,
.selected-panel,
.list-panel {
  padding: 16px;
}

.stat-row,
.legend-row,
.settlement-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
  border-bottom: 1px solid #edf2f7;
}

.stat-row:last-child,
.legend-row:last-child,
.settlement-row:last-child {
  border-bottom: 0;
}

.stat-row span,
.legend-row span {
  color: #64748b;
}

.legend-row {
  justify-content: flex-start;
}

.legend-row i {
  width: 34px;
  height: 18px;
  border-radius: 999px;
  border: 1px solid rgba(15, 23, 42, 0.22);
  flex: 0 0 auto;
}

.bottom-grid {
  display: grid;
  grid-template-columns: 1.3fr 1fr 1fr;
  gap: 14px;
}

.list-panel {
  max-height: 440px;
  overflow: auto;
}

.settlement-row {
  width: 100%;
  border: 0;
  background: transparent;
  color: inherit;
  text-align: right;
}

.settlement-row:hover {
  background: #f8fafc;
}

.settlement-row span {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.settlement-row b {
  direction: ltr;
  white-space: nowrap;
}

@media (max-width: 1100px) {
  .content-grid,
  .bottom-grid {
    grid-template-columns: 1fr;
  }

  .side-panel {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }
}

@media (max-width: 760px) {
  .page-shell {
    padding: 10px;
  }

  .hero {
    flex-direction: column;
    align-items: stretch;
  }

  .hero-actions button,
  .controls label,
  .controls .search-box {
    width: 100%;
    min-width: 0;
  }

  .map-card {
    min-height: 72vh;
  }

  .map {
    height: 72vh;
  }
}
