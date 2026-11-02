// Spelarmodeller för de 6 rollerna i grottmålningsstil (toon-shading + svarta konturer).
// Samma kännetecken som art/grottmalning_roller.svg: färg · kroppsform · siluett · symbol.
// Modellen tittar mot +Z. userData.legs/arms är pivotar (höft/axel) för animation.
(function () {
  'use strict';
  const PAL = { red: 0x9a321e, yel: 0xc98a1f, blk: 0x231812, wht: 0xf3e8cf, brn: 0x6b3f22 };
  const grad = new THREE.DataTexture(new Uint8Array([110, 185, 255]), 3, 1, THREE.RedFormat);
  grad.minFilter = grad.magFilter = THREE.NearestFilter; grad.needsUpdate = true;
  const M = {}; const toon = c => (M[c] = M[c] || new THREE.MeshToonMaterial({ color: c, gradientMap: grad }));
  const outlineMat = new THREE.MeshBasicMaterial({ color: PAL.blk, side: THREE.BackSide });

  function outline(obj, k = 1.1) {
    const meshes = []; obj.traverse(m => { if (m.isMesh && !m.userData.isOutline && !m.userData.noOutline) meshes.push(m); });
    for (const m of meshes) { const o = new THREE.Mesh(m.geometry, outlineMat); o.userData.isOutline = true; o.scale.setScalar(k); m.add(o); }
    return obj;
  }
  function P(geo, c, x, y, z, s = [1, 1, 1], r = [0, 0, 0]) {
    const m = new THREE.Mesh(geo, typeof c === 'number' ? toon(c) : c);
    m.position.set(x, y, z); m.scale.set(...s); m.rotation.set(...r); m.castShadow = true; return m;
  }
  function limb(parent, x, y, z, len, r, c) {
    const pivot = new THREE.Group(); pivot.position.set(x, y, z);
    pivot.add(P(new THREE.CylinderGeometry(r, r * 0.85, len, 6), c, 0, -len / 2, 0));
    parent.add(pivot); pivot.userData.len = len; return pivot;
  }
  const sph = (r, d = 1) => new THREE.IcosahedronGeometry(r, d);
  const cyl = (a, b, h, n = 7) => new THREE.CylinderGeometry(a, b, h, n);
  const cone = (r, h, n = 5) => new THREE.ConeGeometry(r, h, n);

  // ---------------- JÄGAREN: röd · lång och smal · omvänd triangel · vargöron · spjut
  function hunter() {
    const g = new THREE.Group(), c = PAL.red;
    const legs = [limb(g, -0.1, 0.95, 0, 0.95, 0.06, c), limb(g, 0.1, 0.95, 0, 0.95, 0.06, c)];
    g.add(P(cone(0.34, 0.8, 6), c, 0, 1.33, 0, [1, 1, 0.7], [Math.PI, 0, 0]));
    for (const [y, r] of [[1.6, 0.27], [1.45, 0.2], [1.3, 0.13]]) g.add(P(new THREE.TorusGeometry(r, 0.022, 4, 7), PAL.blk, 0, y, 0, [1, 0.7, 1], [Math.PI / 2, 0, 0]));
    g.add(P(sph(0.16), c, 0, 1.88, 0));
    for (const x of [-0.08, 0.08]) g.add(P(cone(0.05, 0.16, 4), c, x, 2.06, 0));
    const arms = [limb(g, -0.26, 1.62, 0, 0.72, 0.05, c), limb(g, 0.26, 1.62, 0, 0.72, 0.05, c)];
    const spear = new THREE.Group(); spear.position.set(0, -0.7, 0.05);
    spear.add(P(cyl(0.025, 0.025, 2.3, 5), PAL.blk, 0, 0.75, 0));
    spear.add(P(cone(0.06, 0.2, 4), PAL.blk, 0, 1.98, 0));
    arms[1].add(spear);
    return finish(g, legs, arms, 'Jägaren', PAL.red);
  }

  // ---------------- SAMLAREN: gul · liten och rund · cirkelkropp · blomkrona · korg på ryggen
  function gatherer() {
    const g = new THREE.Group(), c = PAL.yel;
    const legs = [limb(g, -0.15, 0.58, 0, 0.58, 0.09, c), limb(g, 0.15, 0.58, 0, 0.58, 0.09, c)];
    g.add(P(sph(0.44, 1), c, 0, 0.98, 0, [1, 1, 0.85]));
    g.add(P(new THREE.TorusGeometry(0.24, 0.025, 4, 14), PAL.blk, 0, 0.98, 0.36));
    g.add(P(new THREE.TorusGeometry(0.1, 0.025, 4, 10), PAL.blk, 0, 0.98, 0.37));
    g.add(P(sph(0.2), c, 0, 1.55, 0.02));
    for (let i = 0; i < 4; i++) {                                     // blomkrona
      const a = -0.9 + i * 0.6;
      g.add(P(cyl(0.012, 0.012, 0.2, 4), PAL.blk, Math.sin(a) * 0.17, 1.78, 0, [1, 1, 1], [0, 0, -a * 0.8]));
      g.add(P(sph(0.055, 0), PAL.red, Math.sin(a) * 0.24, 1.9, 0));
    }
    const basket = P(cyl(0.27, 0.2, 0.6, 9), PAL.brn, 0, 1.18, -0.5, [1, 1, 0.8]);
    g.add(basket);
    for (let i = 0; i < 3; i++) g.add(P(new THREE.TorusGeometry(0.24 - i * 0.02, 0.018, 3, 12), PAL.blk, 0, 1.38 - i * 0.18, -0.5, [1, 0.8, 1], [Math.PI / 2, 0, 0]));
    for (const [x, z] of [[-0.08, -0.48], [0.08, -0.55], [0, -0.42], [0.1, -0.44]]) g.add(P(sph(0.06, 0), PAL.red, x, 1.52, z));
    const arms = [limb(g, -0.4, 1.22, 0, 0.5, 0.07, c), limb(g, 0.4, 1.22, 0, 0.5, 0.07, c)];
    return finish(g, legs, arms, 'Samlaren', PAL.yel);
  }

  // ---------------- BYGGAREN: svart · kort och bred · rektangel · stock över huvudet
  function builder() {
    const g = new THREE.Group(), c = PAL.blk;
    const legs = [];
    for (const x of [-0.24, 0.24]) {
      const pv = new THREE.Group(); pv.position.set(x, 0.62, 0);
      pv.add(P(new THREE.BoxGeometry(0.26, 0.62, 0.3), c, 0, -0.31, 0)); g.add(pv); legs.push(pv);
    }
    g.add(P(new THREE.BoxGeometry(1.0, 0.72, 0.52), c, 0, 0.98, 0));
    for (const y of [0.8, 0.98, 1.16]) g.add(P(new THREE.BoxGeometry(1.02, 0.06, 0.54), PAL.yel, 0, y, 0));
    g.add(P(sph(0.21), c, 0, 1.52, 0));
    const arms = [];
    for (const s of [-1, 1]) {                                       // armarna uppsträckta
      const pv = limb(g, s * 0.46, 1.28, 0, 0.62, 0.1, c); pv.rotation.z = s * 2.75; arms.push(pv);
    }
    g.add(P(cyl(0.15, 0.15, 2.3, 8), PAL.red, 0, 1.92, 0, [1, 1, 1], [0, 0, Math.PI / 2]));
    g.add(P(cyl(0.155, 0.155, 0.02, 10), PAL.wht, -1.16, 1.92, 0, [1, 1, 1], [0, 0, Math.PI / 2]));
    return finish(g, legs, arms, 'Byggaren', PAL.blk, { armsStatic: true });
  }

  // ---------------- HANTVERKAREN: vit med svart kontur · romb · spretig hårknut · flinta
  function crafter() {
    const g = new THREE.Group(), c = PAL.wht;
    const legs = [limb(g, -0.12, 0.85, 0, 0.85, 0.07, c), limb(g, 0.12, 0.85, 0, 0.85, 0.07, c)];
    g.add(P(new THREE.OctahedronGeometry(0.42, 0), c, 0, 1.3, 0, [0.9, 1.15, 0.6]));
    g.add(P(new THREE.BoxGeometry(0.025, 0.7, 0.02), PAL.blk, 0, 1.3, 0.24));
    g.add(P(sph(0.18), c, 0, 1.92, 0));
    for (let i = 0; i < 7; i++) {                                    // spretig hårknut
      const a = -1.2 + i * 0.4;
      g.add(P(cone(0.03, 0.2, 4), PAL.blk, Math.sin(a) * 0.17, 1.92 + Math.cos(a) * 0.17, 0, [1, 1, 1], [0, 0, -a]));
    }
    const arms = [limb(g, -0.3, 1.58, 0, 0.66, 0.06, c), limb(g, 0.3, 1.58, 0, 0.66, 0.06, c)];
    arms[1].add(P(sph(0.1, 0), PAL.blk, 0, -0.7, 0.04, [1.3, 1, 1]));      // knacksten
    arms[0].add(P(new THREE.TetrahedronGeometry(0.11), PAL.blk, 0, -0.7, 0.04)); // flinta
    return finish(g, legs, arms, 'Hantverkaren', PAL.wht);
  }

  // ---------------- SPEJAREN: brun · bara streck, längst · tre fjädrar · slunga
  function scout() {
    const g = new THREE.Group(), c = PAL.brn;
    const legs = [limb(g, -0.08, 1.1, 0, 1.1, 0.045, c), limb(g, 0.08, 1.1, 0, 1.1, 0.045, c)];
    g.add(P(cyl(0.075, 0.06, 0.82, 6), c, 0, 1.5, 0, [1, 1, 1], [0.12, 0, 0]));
    g.add(P(sph(0.14), c, 0, 2.06, 0.06));
    [[PAL.red, -0.35], [PAL.blk, 0], [PAL.red, 0.35]].forEach(([col, a], i) => {   // tre fjädrar bakåt
      g.add(P(cone(0.05, 0.5, 4), col, Math.sin(a) * 0.08, 2.28 - i * 0.03, -0.18, [1, 1, 0.3], [-0.9, a, 0]));
    });
    const arms = [limb(g, -0.14, 1.86, 0, 0.8, 0.04, c), limb(g, 0.14, 1.86, 0, 0.8, 0.04, c)];
    const sling = new THREE.Group(); sling.position.set(0, -0.8, 0);
    sling.add(P(cyl(0.008, 0.008, 0.5, 3), PAL.wht, 0, -0.25, 0));
    sling.add(P(sph(0.06, 0), PAL.blk, 0, -0.5, 0));
    arms[1].add(sling);
    return finish(g, legs, arms, 'Spejaren', PAL.brn);
  }

  // ---------------- SHAMANEN: röd med vita prickar · bred mantel · jättehorn · armar uppåt
  function shaman() {
    const g = new THREE.Group(), c = PAL.red;
    const legs = [limb(g, -0.14, 0.3, 0, 0.3, 0.07, c), limb(g, 0.14, 0.3, 0, 0.3, 0.07, c)];
    g.add(P(cyl(0.13, 0.6, 1.3, 9), c, 0, 0.92, 0));
    for (let row = 0; row < 5; row++) {                              // vita prickar
      const y = 0.45 + row * 0.22, r = 0.6 - (y - 0.27) / 1.3 * 0.47 + 0.02;
      const n = 9 - row;
      for (let i = 0; i < n; i++) {
        const a = (i / n) * Math.PI * 2 + row * 0.3;
        const d = P(sph(0.04, 0), PAL.wht, Math.sin(a) * r, y, Math.cos(a) * r); d.userData.noOutline = true; g.add(d);
      }
    }
    g.add(P(sph(0.18), c, 0, 1.75, 0));
    for (const s of [-1, 1]) {                                       // stora grenade horn
      g.add(P(cyl(0.03, 0.035, 0.6, 5), PAL.blk, s * 0.2, 2.08, 0, [1, 1, 1], [0, 0, -s * 0.5]));
      g.add(P(cyl(0.025, 0.03, 0.5, 5), PAL.blk, s * 0.36, 2.52, 0, [1, 1, 1], [0, 0, -s * 0.15]));
      g.add(P(cyl(0.02, 0.025, 0.32, 5), PAL.blk, s * 0.5, 2.3, 0, [1, 1, 1], [0, 0, -s * 1.2]));
      g.add(P(cyl(0.02, 0.02, 0.28, 5), PAL.blk, s * 0.28, 2.82, 0, [1, 1, 1], [0, 0, s * 0.5]));
    }
    const arms = [];
    for (const s of [-1, 1]) { const pv = limb(g, s * 0.2, 1.48, 0, 0.75, 0.055, c); pv.rotation.z = s * 2.5; arms.push(pv); }
    return finish(g, legs, arms, 'Shamanen', PAL.red, { armsStatic: true });
  }

  function finish(g, legs, arms, role, color, extra = {}) {
    outline(g);
    const root = new THREE.Group(); root.add(g);
    root.userData = Object.assign({ role, color, legs, arms, body: g, baseArmZ: arms.map(a => a.rotation.z) }, extra);
    root.traverse(m => { if (m.isMesh) m.castShadow = true; });
    return root;
  }

  // Gånganimation: phase = tid * hastighet, amount 0..1 (0 = står still)
  function pose(p, phase, amount = 1) {
    const u = p.userData, s = Math.sin(phase) * 0.65 * amount;
    u.legs[0].rotation.x = s; u.legs[1].rotation.x = -s;
    if (!u.armsStatic) { u.arms[0].rotation.x = -s * 0.8; u.arms[1].rotation.x = s * 0.8; }
    u.body.position.y = Math.abs(Math.cos(phase)) * 0.06 * amount;
  }
  // Slungad genom luften: armar och ben far åt alla håll
  function flail(p, t) {
    const u = p.userData;
    u.arms[0].rotation.set(Math.sin(t * 9) * 0.5, 0, -2.6 + Math.sin(t * 7) * 0.3);
    u.arms[1].rotation.set(Math.cos(t * 8) * 0.5, 0, 2.6 + Math.cos(t * 6) * 0.3);
    u.legs[0].rotation.set(Math.sin(t * 10) * 0.9, 0, -0.3);
    u.legs[1].rotation.set(-Math.sin(t * 10) * 0.9, 0, 0.3);
  }
  // Namnskylt med rollens färg ovanför huvudet
  function nameTag(name, role, color) {
    const c = document.createElement('canvas'); c.width = 256; c.height = 64; const g = c.getContext('2d');
    const hex = '#' + color.toString(16).padStart(6, '0');
    g.fillStyle = 'rgba(35,24,18,.82)'; g.beginPath(); g.roundRect(4, 8, 248, 48, 18); g.fill();
    g.fillStyle = hex; g.beginPath(); g.arc(34, 32, 16, 0, 7); g.fill();
    g.strokeStyle = '#f3e8cf'; g.lineWidth = 3; g.stroke();
    g.fillStyle = '#f3e8cf'; g.font = 'bold 22px Georgia'; g.textBaseline = 'middle'; g.fillText(name, 60, 26);
    g.font = '14px Georgia'; g.fillStyle = '#d9c7aa'; g.fillText(role, 60, 46);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace;
    const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, depthTest: false, transparent: true }));
    s.scale.set(1.6, 0.4, 1); s.renderOrder = 10; return s;
  }

  const MAKERS = { 'Jägaren': hunter, 'Samlaren': gatherer, 'Byggaren': builder, 'Hantverkaren': crafter, 'Spejaren': scout, 'Shamanen': shaman };
  window.Players = { ROLES: Object.keys(MAKERS), make: role => MAKERS[role](), pose, flail, nameTag };
})();
