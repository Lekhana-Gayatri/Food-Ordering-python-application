import React, { Component } from 'react'

export class Spinner extends Component {
  render() {
    return (
        <div class="spinner-border text-info" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    )
  }
}

export default Spinner
