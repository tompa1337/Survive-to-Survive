// Djur i grottmålningsstil: toon-shading, svarta konturer, naturpigment.
// Används av index.html (spelet) och djur.html (förhandsvisning).
// Varje djur tittar mot +X. Benen ligger i userData.legs (pivot vid höften) för gånganimation.
(function () {
  'use strict';
  const PAL = { red: 0x9a321e, yel: 0xc98a1f, blk: 0x231812, wht: 0xf3e8cf, brn: 0x6b3f22 };
  const grad = new THREE.DataTexture(new Uint8Array([110, 185, 255]), 3, 1, THREE.RedFormat);
  grad.minFilter = grad.magFilter = THREE.NearestFilter; grad.needsUpdate = true;
  const toon = c => new THREE.MeshToonMaterial({ color: c, gradientMap: grad });
  const flat = c => new THREE.MeshBasicMaterial({ color: c });
  const outlineMat = new THREE.MeshBasicMaterial({ color: PAL.blk, side: THREE.BackSide });

  function outline(obj, k) {
    const meshes = []; obj.traverse(m => { if (m.isMesh && !m.userData.isOutline && !m.userData.noOutline) meshes.push(m); });
    for (const m of meshes) { const o = new THREE.Mesh(m.geometry, outlineMat); o.userData.isOutline = true; o.scale.setScalar(k); m.add(o); }
    return obj;
  }
  function part(geo, mat, x, y, z, s = [1, 1, 1], r = [0, 0, 0]) {
    const m = new THREE.Mesh(geo, mat); m.position.set(x, y, z); m.scale.set(...s); m.rotation.set(...r); m.castShadow = true; return m;
  }
  function legs(g, mat, hipY, len, r, xs, zs, hoof) {
    const list = [];
    for (const x of xs) for (const z of zs) {
      const pivot = new THREE.Group(); pivot.position.set(x, hipY, z);
      pivot.add(part(new THREE.CylinderGeometry(r, r * 0.75, len, 6), mat, 0, -len / 2, 0));
      if (hoof) pivot.add(part(new THREE.CylinderGeometry(r * 0.8, r * 0.9, len * 0.14, 6), hoof, 0, -len + len * 0.05, 0));
      g.add(pivot); list.push(pivot);
    }
    return list;
  }
  const eye = (g, x, y, z, c) => { const e = part(new THREE.SphereGeometry(0.04, 6, 6), flat(c), x, y, z); e.userData.noOutline = true; g.add(e); };

  // ---------------- VARG: askgrå, smal, lång nos, spetsiga öron, röd ockra-rand på ryggen
  function makeWolf() {
    const g = new THREE.Group();
    const fur = toon(0x6e665e), light = toon(PAL.wht), dark = toon(PAL.blk), red = toon(PAL.red);
    g.add(part(new THREE.IcosahedronGeometry(0.5, 0), fur, 0, 0.88, 0, [1.5, 0.72, 0.62]));
    g.add(part(new THREE.IcosahedronGeometry(0.34, 0), light, 0.42, 0.86, 0, [0.9, 1, 0.95]));          // ljus bröstkrage
    g.add(part(new THREE.BoxGeometry(1.0, 0.05, 0.14), red, -0.05, 1.22, 0));                            // målad rand
    for (let i = 0; i < 4; i++) g.add(part(new THREE.ConeGeometry(0.07, 0.16, 4), red, -0.4 + i * 0.26, 1.27, 0)); // sicksack
    g.add(part(new THREE.IcosahedronGeometry(0.27, 0), fur, 0.88, 1.12, 0, [1.15, 0.9, 0.85]));         // huvud
    g.add(part(new THREE.ConeGeometry(0.13, 0.42, 5), light, 1.22, 1.04, 0, [1, 1, 1], [0, 0, -Math.PI / 2])); // nos
    g.add(part(new THREE.SphereGeometry(0.05, 6, 6), dark, 1.43, 1.04, 0));
    for (const z of [-0.12, 0.12]) g.add(part(new THREE.ConeGeometry(0.07, 0.22, 4), fur, 0.8, 1.38, z));  // öron
    g.add(part(new THREE.ConeGeometry(0.12, 0.62, 5), fur, -0.86, 0.86, 0, [1, 1, 1], [0, 0, Math.PI / 2 + 0.55])); // svans
    g.add(part(new THREE.ConeGeometry(0.07, 0.18, 5), light, -1.1, 0.68, 0, [1, 1, 1], [0, 0, Math.PI / 2 + 0.55]));
    const L = legs(g, fur, 0.66, 0.62, 0.065, [0.42, -0.42], [0.16, -0.16], dark);
    outline(g, 1.09);
    for (const z of [-0.11, 0.11]) eye(g, 1.08, 1.17, z, PAL.red);
    g.userData = { kind: 'wolf', legs: L, speed: 7, hp: 30 };
    return g;
  }

  // ---------------- BJÖRN: umbrabrun, massiv, puckel, runda öron, gul nos
  function makeBear() {
    const g = new THREE.Group();
    const fur = toon(PAL.brn), muzzle = toon(PAL.yel), dark = toon(PAL.blk), claw = toon(PAL.wht);
    g.add(part(new THREE.IcosahedronGeometry(0.8, 1), fur, 0, 1.2, 0, [1.4, 0.92, 0.92]));
    g.add(part(new THREE.IcosahedronGeometry(0.48, 1), fur, 0.38, 1.82, 0, [1.2, 0.8, 1]));               // skulderpuckel
    g.add(part(new THREE.IcosahedronGeometry(0.5, 1), muzzle, 0.2, 0.95, 0, [1.5, 0.6, 0.8]));             // ljus buk
    g.add(part(new THREE.IcosahedronGeometry(0.42, 1), fur, 1.32, 1.42, 0, [1.05, 0.95, 1]));             // huvud
    g.add(part(new THREE.IcosahedronGeometry(0.22, 1), muzzle, 1.7, 1.3, 0, [1.3, 0.8, 0.95]));            // nos
    g.add(part(new THREE.SphereGeometry(0.08, 6, 6), dark, 1.96, 1.34, 0));
    for (const z of [-0.26, 0.26]) {
      g.add(part(new THREE.SphereGeometry(0.13, 6, 6), fur, 1.22, 1.8, z));                                // runda öron
      g.add(part(new THREE.SphereGeometry(0.06, 6, 6), dark, 1.25, 1.8, z * 1.05));
    }
    const L = legs(g, fur, 0.85, 0.85, 0.18, [0.65, -0.62], [0.38, -0.38], dark);
    for (const z of [0.38, -0.38]) for (let i = -1; i <= 1; i++)                                          // klor
      g.add(part(new THREE.ConeGeometry(0.03, 0.12, 4), claw, 0.86, 0.04, z + i * 0.07, [1, 1, 1], [0, 0, -Math.PI / 2]));
    outline(g, 1.06);
    for (const z of [-0.17, 0.17]) eye(g, 1.66, 1.5, z, PAL.blk);
    g.userData = { kind: 'bear', legs: L, speed: 5, hp: 90 };
    return g;
  }

  // ---------------- VILDSVIN: mörk rödbrun, tunnformad, svart borstman, vita betar, platt tryne
  function makeBoar() {
    const g = new THREE.Group();
    const hide = toon(0x5c2a18), mane = toon(PAL.blk), tusk = toon(PAL.wht), snout = toon(0xb0603a);
    g.add(part(new THREE.IcosahedronGeometry(0.5, 1), hide, 0, 0.72, 0, [1.5, 0.95, 0.85]));
    for (let i = 0; i < 6; i++)                                                                            // borstman
      g.add(part(new THREE.ConeGeometry(0.07, 0.26 - Math.abs(i - 2) * 0.03, 4), mane, -0.4 + i * 0.17, 1.17 - Math.abs(i - 3) * 0.02, 0));
    g.add(part(new THREE.CylinderGeometry(0.12, 0.3, 0.62, 7), hide, 0.86, 0.7, 0, [1, 1, 1], [0, 0, -Math.PI / 2])); // kilformat huvud
    g.add(part(new THREE.CylinderGeometry(0.14, 0.14, 0.07, 8), snout, 1.18, 0.68, 0, [1, 1, 1], [0, 0, -Math.PI / 2])); // tryne
    for (const z of [-0.11, 0.11]) {
      g.add(part(new THREE.ConeGeometry(0.035, 0.22, 5), tusk, 1.07, 0.66, z, [1, 1, 1], [0, 0, -0.45]));  // betar
      g.add(part(new THREE.ConeGeometry(0.07, 0.17, 4), hide, 0.66, 0.98, z * 1.4, [1, 1, 1], [z * 2, 0, 0.3])); // öron
    }
    g.add(part(new THREE.CylinderGeometry(0.02, 0.02, 0.3, 4), mane, -0.82, 0.72, 0, [1, 1, 1], [0, 0, 0.8])); // svans
    const L = legs(g, hide, 0.45, 0.46, 0.065, [0.4, -0.42], [0.17, -0.17], mane);
    outline(g, 1.08);
    for (const z of [-0.12, 0.12]) eye(g, 0.94, 0.84, z, PAL.red);
    g.userData = { kind: 'boar', legs: L, speed: 6, hp: 45 };
    return g;
  }

  window.Animals = { makeWolf, makeBear, makeBoar };
})();
