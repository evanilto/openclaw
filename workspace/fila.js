export async function fila() {

  const res = await fetch("http://fila-api:5000/fila");
  return await res.json();

}

export async function posicao(prontuario) {

  const res = await fetch(`http://fila-api:5000/fila/posicao/${prontuario}`);
  return await res.json();

}

export async function primeiro(especialidade) {

  const res = await fetch(`http://fila-api:5000/fila/especialidade/${especialidade}`);
  return await res.json();

}

export async function tempoMedio() {

  const res = await fetch("http://fila-api:5000/fila/tempo-medio");
  return await res.json();

}
