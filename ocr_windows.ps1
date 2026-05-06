Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

[Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType = WindowsRuntime] | Out-Null

$pdf = "C:\Users\Administrator\.qclaw\workspace\company-website\luminescence.pdf"

try {
    Add-Type -Path "C:\Program Files\Windows Kits\10\References\10.0.19041.0\Windows.Media.Ocr\Windows.Media.Ocr.dll" -ErrorAction Stop
} catch {
    Write-Host "Windows.Media.Ocr DLL not found, trying alternative..."
}

Add-Type -AssemblyName PresentationCore

$bitmap = [System.Drawing.Bitmap]::FromFile($pdf)

# Try to use Windows.Media.Ocr
$language = New-Object Windows.Media.Ocr.OcrLanguage("zh-CN")
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($language)

if ($engine) {
    $asyncOp = $engine.RecognizeAsync($bitmap)
    $asyncOp.Wait()
    $result = $asyncOp.GetResults()
    $result.Lines | ForEach-Object { $_.Text }
} else {
    Write-Host "OcrEngine not available"
}

$bitmap.Dispose()
