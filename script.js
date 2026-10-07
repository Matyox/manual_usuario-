// ============================================================
// MANUAL INTERACTIVO — JavaScript
// ============================================================

// ============================================================
// DATOS DEL BUFFER (hex del programa)
// ============================================================
const BUFFER_HEX = `
3D 3D 3D 20 41 4E 41 4C 49 5A 41 44 4F 52 20 44 45 20 49 4E 54 45 52 46 45 52 45 4E
43 49 41 20 45 4E 20 50 45 4C 49 43 55 4C 41 53 20 44 45 4C 47 41 44 41 53 20 3D 3D
3D 0D 0A 45 73 70 65 73 6F 72 3A 20 33 32 30 20 6E 6D 20 7C 20 49 6E 64 69 63 65 20
64 65 20 72 65 66 72 61 63 63 69 6F 6E 3A 20 31 2E 33 33 0D 0A 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F 72 64 65 6E 20 6D 20
3D 20 30 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 3A 20 31 37
30 32 2E 34 30 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46 55 45 52 41 20 44 45 4C 20 45
53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D 0A 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F 72 64 65 6E 20 6D 20 3D 20 31
20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 3A 20 35 36 37 2E 34
36 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 56 49 53 49 42 4C 45 5D 20 45 73 74 61 20 6C
6F 6E 67 69 74 75 64 20 64 65 20 6F 6E 64 61 20 73 65 20 72 65 66 6C 65 6A 61 2E
0D 0A 20 20 2D 3E 20 43 6F 6C 6F 72 20 61 70 72 6F 78 69 6D 61 64 6F 3A 20 56 65
72 64 65 0D 0A 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 0D 0A 4F 72 64 65 6E 20 6D 20 3D 20 32 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20
64 65 20 6F 6E 64 61 3A 20 33 34 30 2E 34 38 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46
55 45 52 41 20 44 45 4C 20 45 53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D
0A 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 4F
72 64 65 6E 20 6D 20 3D 20 33 20 2D 3E 20 4C 6F 6E 67 69 74 75 64 20 64 65 20 6F
6E 64 61 3A 20 32 34 33 2E 32 30 20 6E 6D 0D 0A 20 20 2D 3E 20 5B 46 55 45 52 41
20 44 45 4C 20 45 53 50 45 43 54 52 4F 20 56 49 53 49 42 4C 45 5D 0D 0A 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D
2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 0D 0A 3D 3D
3D 20 46 49 4E 20 44 45 4C 20 41 4E 41 4C 49 53 49 53 20 3D 3D 3D 0D 0A
`;

// ============================================================
// FUNCIONES AUXILIARES
// ============================================================
function hexAChar(hex) {
    const n = parseInt(hex, 16);
    if (n === 0x0D) return '␍';
    if (n === 0x0A) return '␊';
    if (n >= 32 && n <= 126) return String.fromCharCode(n);
    return '·';
}

function mostrarPlaceholder(img) {
    img.style.display = 'none';
    img.nextElementSibling.style.display = 'block';
}

// ============================================================
// NAVEGACIÓN POR PESTAÑAS
// ============================================================
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        // Quitar active de todos
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

        // Activar el seleccionado
        btn.classList.add('active');
        const tabId = btn.dataset.tab;
        document.getElementById(tabId).classList.add('active');

        // Scroll al inicio
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});

// ============================================================
// BUFFER INTERACTIVO
// ============================================================
const bytesHex = BUFFER_HEX.trim().split(/\s+/);
let revelados = new Array(bytesHex.length).fill(false);
const botonesBytes = [];

const gridBuffer = document.getElementById('grid-buffer');
const estadoBuffer = document.getElementById('estado-buffer');
const textoRevelado = document.getElementById('texto-revelado');

// Crear botones de byte
bytesHex.forEach((hex, i) => {
    const btn = document.createElement('button');
    btn.className = 'byte-btn';
    btn.textContent = hex;
    btn.dataset.index = i;
    btn.addEventListener('click', () => revelarByte(i));
    gridBuffer.appendChild(btn);
    botonesBytes.push(btn);
});

// Actualizar estado inicial
actualizarEstado();

function revelarByte(idx) {
    if (revelados[idx]) return;
    revelados[idx] = true;
    const hex = bytesHex[idx];
    const char = hexAChar(hex);
    botonesBytes[idx].classList.add('revelado');
    botonesBytes[idx].innerHTML = `${hex}<br>${char}`;
    actualizarEstado();
    actualizarTexto();
}

function revelarTodo() {
    bytesHex.forEach((hex, i) => {
        if (!revelados[i]) {
            revelados[i] = true;
            const char = hexAChar(hex);
            botonesBytes[i].classList.add('revelado');
            botonesBytes[i].innerHTML = `${hex}<br>${char}`;
        }
    });
    actualizarEstado();
    actualizarTexto();
}

function reiniciarBuffer() {
    bytesHex.forEach((hex, i) => {
        revelados[i] = false;
        botonesBytes[i].classList.remove('revelado');
        botonesBytes[i].textContent = hex;
    });
    actualizarEstado();
    actualizarTexto();
}

function actualizarEstado() {
    const n = revelados.filter(Boolean).length;
    estadoBuffer.textContent = `${n} / ${bytesHex.length} revelados`;
}

function actualizarTexto() {
    let texto = '';
    bytesHex.forEach((hex, i) => {
        texto += revelados[i] ? hexAChar(hex) : '·';
    });
    texto = texto.replace(/␍/g, '').replace(/␊/g, '\n');
    textoRevelado.textContent = texto;
}

// Botones de control
document.getElementById('btn-revelar-todo').addEventListener('click', revelarTodo);
document.getElementById('btn-reiniciar').addEventListener('click', reiniciarBuffer);

// ============================================================
// SMOOTH SCROLL EN TABS
// ============================================================
console.log('✅ Manual HTML cargado correctamente');