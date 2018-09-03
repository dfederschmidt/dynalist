# dynalist

Python CLI and libary for [dynalist.io](https://dynalist.io) based on the [Dynalist API](https://apidocs.dynalist.io/#introduction).
Documentation available on [Github Pages](https://dfederschmidt.github.io/dynalist/).

## Testing

To run the test suite, run
```bash
python -m unittest
```


## CLI Usage

Get the token from https://dynalist.io/developer and enter for the tool to use by running
```bash
dynalist token
```

Fetch all documents
```bash
dynalist docs
```

Fetch all folders
```bash
dynalist folders
```

## Library Usage
You can also interact with dynalist programatically.

```python
import dynalist

dyn = Dynalist("yourtokenhere")
dyn.all()
dyn.doc("documentid")
dyn.to_inbox("Item to add", "Optional note")
```