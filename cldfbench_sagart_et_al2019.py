import pathlib

import phlorest


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
            self.raw_dir.read_nexus('sino-tibetan-beastwords.nex'),
            self.characters, 
            args.log)
