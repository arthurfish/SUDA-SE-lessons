# ruff: noqa: N999

from torch import nn
from torchcrf import CRF


class NERLSTM_CRF(nn.Module):  # noqa: N801
    def __init__(self, embedding_dim, hidden_dim, dropout, word2id, tag2id):  # noqa: PLR0913
        super().__init__()

        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.vocab_size = len(word2id) + 1
        self.tag_to_ix = tag2id
        self.tagset_size = len(tag2id)

        self.word_embeds = nn.Embedding(self.vocab_size, self.embedding_dim)
        self.dropout = nn.Dropout(dropout)

        # CRF
        self.lstm = nn.LSTM(
            self.embedding_dim,
            self.hidden_dim // 2,
            num_layers=1,
            bidirectional=True,
            batch_first=False,
        )

        self.hidden2tag = nn.Linear(self.hidden_dim, self.tagset_size)
        self.crf = CRF(self.tagset_size)

    def forward(self, x):
        # CRF
        x = x.transpose(0, 1)
        x.size(1)
        x.size(0)

        embedding = self.word_embeds(x)
        outputs, _ = self.lstm(embedding)
        outputs = self.dropout(outputs)
        outputs = self.hidden2tag(outputs)

        # CRF
        return self.crf.decode(outputs)

    def log_likelihood(self, x, tags):
        x = x.transpose(0, 1)
        x.size(1)
        x.size(0)
        tags = tags.transpose(0, 1)
        embedding = self.word_embeds(x)
        outputs, _ = self.lstm(embedding)
        outputs = self.dropout(outputs)
        outputs = self.hidden2tag(outputs)
        return -self.crf(outputs, tags.long())
