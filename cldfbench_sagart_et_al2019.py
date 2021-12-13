import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "sagart_et_al2019"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'sinotibetan-beast-covarion-relaxed-fbd.mcct.trees', detranslate=True),
            self.metadata,
            args.log)

        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('sinotibetan-march-beast-covarion-relaxed-fbd.trees.gz'),
                1000),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees, 
            self.metadata, 
            args.log)
            
        args.writer.add_data(
            self.raw_dir.read_nexus('sino-tibetan-beastwords.nex'),
            self.characters, 
            args.log)
