export const toRna = (sequence) => {
   return sequence.split('').map(nucleotide => {
      if (nucleotide == '') return ''
      if (nucleotide == 'C') return 'G'
      if (nucleotide == 'G') return 'C'
      if (nucleotide == 'T') return 'A'
      if (nucleotide == 'A') return 'U'
   }).join('')
};
