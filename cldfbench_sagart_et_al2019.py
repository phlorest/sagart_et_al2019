import re
import pathlib
import collections

import phlorest


class FixNexus:
    def __init__(self):
        self.c = collections.Counter()
        self.p = re.compile('\s+(?P<num>[0-9]+)\s+(?P<concept>[^,]+),?')

    def __call__(self, s):
        lines = []
        for line in s.split('\n'):
            m = self.p.fullmatch(line)
            if m:
                self.c.update([m.group('concept')])
                comma = ',' if line.strip().endswith(',') else ''
                line = '\t{} {}_{}{}'.format(
                    m.group('num'),
                    m.group('concept'),
                    self.c[m.group('concept')],
                    comma)
            lines.append(line)
        return '\n'.join(lines)


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "sagart_et_al2019"

    def cmd_makecldf(self, args):
        self.init(args)
        
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'sinotibetan-beast-covarion-relaxed-fbd.mcct.trees',
                detranslate=True),
            self.metadata,
            args.log)

        posterior = self.raw_dir.read_trees(
            'sinotibetan-march-beast-covarion-relaxed-fbd.trees.gz',
            burnin=1001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus(
                'sino-tibetan-beastwords.nex',
                preprocessor=FixNexus()),
            self.characters, 
            args.log)
