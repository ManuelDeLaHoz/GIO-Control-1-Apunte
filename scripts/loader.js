import fs from 'fs';
import path from 'path';

const slidesDir = './diapositivas';
const templateFile = './template.html';
const outputFile = './index.html';

if (!fs.existsSync(slidesDir)) {
    fs.mkdirSync(slidesDir);
}

const files = fs.readdirSync(slidesDir)
    .filter(f => f.endsWith('.html'))
    .sort((a, b) => parseInt(a) - parseInt(b));

const slidesHtml = files.map(file => {
    return `                <section data-background-iframe="diapositivas/${file}" data-background-interactive></section>`;
}).join('\n');

if (fs.existsSync(templateFile)) {
    let template = fs.readFileSync(templateFile, 'utf8');
    
    // CAMBIO CLAVE: Ahora sí buscamos el marcador exacto
 // Ahora buscamos la palabra exacta en lugar de comillas vacías
const finalHtml = template.replace('REEMPLAZAR_AQUI', slidesHtml);
    
    fs.writeFileSync(outputFile, finalHtml);
    console.log(`✅ index.html actualizado con ${files.length} diapositivas.`);
}